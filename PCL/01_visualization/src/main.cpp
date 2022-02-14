#include <iostream>
#include <pcl/io/pcd_io.h>
#include <pcl/visualization/cloud_viewer.h>

int main(int argc, char *argv[])
{
    pcl::PointCloud<pcl::PointXYZRGB>::Ptr showPoints(new pcl::PointCloud<pcl::PointXYZRGB>);
    pcl::io::loadPCDFile("../../data/teacup.pcd", *showPoints);

    pcl::visualization::CloudViewer viewer("Clouds");

    viewer.showCloud(showPoints);

    while (!viewer.wasStopped()) {
       //因為這邊是和visualization的視窗同步跑，所以可以在之中執行一些處理
    }

    return 0;
}
