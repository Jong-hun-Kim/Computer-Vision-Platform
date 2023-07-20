import Function_Library as fl

EPOCH = 500000

if __name__ == "__main__":
    # Exercise Environment Setting
    env = fl.libCAMERA()

    """ Exercise 1: RGB Color Value Extracting """
    ############## YOU MUST EDIT ONLY HERE ##############
    example = env.file_read("./Example Image.jpg")
    # R, G, B = env.extract_rgb(example, print_enable=True)
    # quit()
    #####################################################

    # Camera Initial Setting
    ch0, ch1 = env.initial_setting(cam0port=1, cam1port=2, capnum=2)

    # Camera Reading..
    for i in range(EPOCH):
        _, frame0, _, frame1 = env.camera_read(ch0, ch1)

        np_frame0 = fl.np.array(example)
        print(np_frame0.shape)

        """ Exercise 2: Webcam Real-time Reading """
        ############## YOU MUST EDIT ONLY HERE ##############
        # env.image_show(frame0, frame1)
        #####################################################

        env.number_tracking(frame0)

        """ Exercise 3: Object Detection (Traffic Light Circle) """
        #################### YOU MUST EDIT ONLY HERE ####################
        # color = env.object_detection(frame0, sample=16, print_enable=True)
        #################################################################

        """ Exercise 4: Specific Edge Detection (Traffic Line) """
        #################### YOU MUST EDIT ONLY HERE ####################
        # direction = env.edge_detection(frame0, width=500, height=120,
        #                                gap=40, threshold=150, print_enable=False)
        #################################################################

        # Process Termination (If you input the 'q', camera scanning is ended.)
        if env.loop_break():
            break
