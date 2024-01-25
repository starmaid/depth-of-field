# Lytro Illum effect with a $180 depth camera. Do it live.
# this is just video game depth of field implemented on the real world
# https://www.youtube.com/watch?v=v9x_50czf-4


import pyrealsense2 as rs
import numpy as np
import cv2

pipeline = rs.pipeline()
config = rs.config()

pipeline_wrapper = rs.pipeline_wrapper(pipeline)
pipeline_profile = config.resolve(pipeline_wrapper)
device = pipeline_profile.get_device()
device_product_line = str(device.get_info(rs.camera_info.product_line))

config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
#config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
config.enable_stream(rs.stream.color, 1920, 1080, rs.format.bgr8, 30)

profile = pipeline.start(config)

depth_sensor = profile.get_device().first_depth_sensor()
depth_scale = depth_sensor.get_depth_scale()
print("Depth Scale is: " , depth_scale)

align_to = rs.stream.color
align = rs.align(align_to)

def getCoC(depth, focus_depth, focus_range):
    nearBegin = max([focus_depth - focus_range, 0])
    farBegin = focus_depth + focus_range
    
    nearCoC = 0
    if depth < focus_depth:
        nearCoC = 1 / (nearBegin - focus_depth) * depth + -1 * focus_depth / (nearBegin - focus_depth);
    elif depth < nearBegin:
        nearCoC = 1
    
    farCoC = 1
    if depth < focus_depth:
        farCoC = 0
    elif depth < farBegin:
        farCOC = 1 / (focus_depth - farBegin) * depth + -farBegin / (focus_depth - farBegin);
    
    triple = np.clip([nearCoC, farCoC, 0], 0, 1)
    
    return(np.clip(nearCoC,0,1))
    #return(triple)
    
def darkenAwayFromFocus(color_image, depth_image, focus_depth, focus_range):
    getCoCV = np.vectorize(getCoC)
    
    CoC = getCoCV(depth_image, focus_depth, focus_range)
    
    
    mask = np.int32(depth_image) - (focus_depth/depth_scale) + 200
    mask_norm = mask / mask.max()
    result = np.uint8(color_image[:,:,0] * mask_norm)
    return(mask)

font = cv2.FONT_HERSHEY_PLAIN

# Streaming loop
try:
    while True:
        # Get frameset of color and depth
        frames = pipeline.wait_for_frames()
        # frames.get_depth_frame() is a 640x360 depth image

        # Align the depth frame to color frame
        aligned_frames = align.process(frames)

        # Get aligned frames
        aligned_depth_frame = aligned_frames.get_depth_frame() # aligned_depth_frame is a 640x480 depth image
        color_frame = aligned_frames.get_color_frame()

        # Validate that both frames are valid
        if not aligned_depth_frame or not color_frame:
            continue

        depth_image = np.asanyarray(aligned_depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        color2 = darkenAwayFromFocus(color_image, depth_image, 0.5, 0.2)

        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(color2, alpha=0.03), cv2.COLORMAP_JET)

        cv2.putText(depth_colormap, f'stuff',(10,50),font,4,(0,0,255),4,cv2.LINE_AA)
        
        cv2.namedWindow('Align Example', cv2.WINDOW_NORMAL)
        cv2.imshow('Align Example', color2)
        key = cv2.waitKey(1)
        # Press esc or 'q' to close the image window
        if key & 0xFF == ord('q') or key == 27:
            cv2.destroyAllWindows()
            break
finally:
    pipeline.stop()

'''
while True:
    depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(CoC, alpha=0.03), cv2.COLORMAP_JET)
    cv2.imshow('Align Example', depth_colormap)
    key = cv2.waitKey(1)
    # Press esc or 'q' to close the image window
    if key & 0xFF == ord('q') or key == 27:
        cv2.destroyAllWindows()
        break
'''