#include <iostream>
#include <string>
#include <unistd.h>

#include <opencv2/opencv.hpp>

#define MAXPATHLEN 256

using std::string;

int main(int argc, char** argv) {
  char cwd[MAXPATHLEN];
  string path, root_path;
  size_t pos;

  if (getcwd(cwd, sizeof(cwd)) != NULL) {
    printf("Current working dir: %s\n", cwd);
    path = string(cwd);
    pos = path.find("build");
    root_path = path.substr(0, pos);
  }

  string image_path = root_path + "/images/dog.jpg";
  cv::Mat image = cv::imread(image_path);
  int w = image.cols;
  int h = image.rows;

  // Output filename
  char out_path[MAXPATHLEN];
  sprintf(out_path, "%simages/test_%dx%d_yuv420p.yuv", root_path.c_str(), w, h);
  FILE* yuv_file = fopen(out_path, "wb");
  if (!yuv_file) {
    printf("File open error!\n");
    exit(-1);
  }

  // Configuration for YUV Buffer
  int buf_length = w * h * 3 / 2; // YUV420
  u_char* yuv_buf = new u_char[buf_length];

  // Using cvtColor convert RGB to YUV420
  //   YU12在Android平臺下又叫I420
  //   BGR -> YU12 (y,u,v排列)
  //   RGB -> YV12 (y,v,u排列)
  //   RGB & YUB: R與V有關, B與U有關
  cv::Mat yuv_img;
  cvtColor(image, yuv_img, CV_BGR2YUV_I420);

  // memory copy image to yuv buf and save file
  memcpy(yuv_buf, yuv_img.data, buf_length * sizeof(unsigned char));
  fwrite(yuv_buf, buf_length * sizeof(unsigned char), 1, yuv_file);
  std::cout << "Convert Done. File save at " << out_path << "\n";

  return 0;
}
