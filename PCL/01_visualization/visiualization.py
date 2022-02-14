import numpy as np
import pcl
import pcl.pcl_visualization


def main():
    cloud = pcl.load_XYZRGB("../data/teacup.pcd")

    viewer = pcl.pcl_visualization.CloudViewing()
    viewer.ShowColorCloud(cloud, b'cloud')

    v = True
    while v:
        v = not(viewer.WasStopped())


if __name__ == "__main__":
    main()
