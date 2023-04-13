import math
import cv2
import numpy as np

# blockSize
bkS = 8
# scale up blocks for easier visualization
mag = 10
    
for u in range(bkS):
    for v in range(bkS):
        # store computed DCT values in this variable
        image = np.zeros((bkS*mag, bkS*mag), np.float32)
        # update these values with the smallest and largest DCT value found for this block
        maxV = -100000.0
        minV = 100000.0
        


        #### fill in DCT calculation ####



        for x in range(bkS):
            for y in range(bkS):
                if u == 0:
                    alpha_u = math.sqrt(1.0/bkS)
                else:
                    alpha_u = math.sqrt(2.0/bkS)

                if v == 0:
                    alpha_v = math.sqrt(1.0/bkS)
                else:
                    alpha_v = math.sqrt(2.0/bkS)

                val = alpha_u*alpha_v*math.cos((2*x+1)*u*math.pi/(2*bkS))*math.cos((2*y+1)*v*math.pi/(2*bkS))
                image[y][x] = val

                # update min and max values
                if val > maxV:
                    maxV = val
                if val < minV:
                    minV = val

        # DCT values need to be mapped to [0-255] for visualization        
        imageN = np.zeros((bkS*mag, bkS*mag), np.float32)
        if maxV == minV:
            for x in range(bkS*mag):
                for y in range(bkS*mag):
                    imageN[y][x] = 255.0
        else:
            for x in range(bkS):
                for m in range(mag):
                    for y in range(bkS):
                        val = 255.0*(image[y][x]-minV)/(maxV-minV)
                        for n in range(mag):
                            imageN[mag*y+n][mag*x+m] = val
                            

        name = "dctPatches/dctPatch_" + str(u) + "_" + str(v) + ".png"
        cv2.imwrite(name, imageN)


