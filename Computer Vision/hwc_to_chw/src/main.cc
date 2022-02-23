#include <iostream>
#include <string>
#include <unistd.h>

#include <opencv2/opencv.hpp>
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/stl.h>

#include "mat_wraper.h"

#define MAXPATHLEN 256

using std::string;
namespace py = pybind11;

py::list hwc2chw() {
  char cwd[MAXPATHLEN];
  std::string path, root_path;
  size_t pos;

  if (getcwd(cwd, sizeof(cwd)) != NULL) {
    printf("Current working dir: %s\n", cwd);
    path = string(cwd);
    pos = path.find("build");
    root_path = path.substr(0, pos);
  }

  std::string image_path = root_path + "/images/dog.jpg";
  std::cout << image_path << "\n";
  cv::Mat image = cv::imread(image_path);

  static const int height = image.size().height;
  static const int width = image.size().width;
  static const int channels = image.channels();
  int dims = image.dims;
  std::cout << "[HWC Image]"
            << " H: " << image.size().height
            << " W: " << image.size().width
            << " C: " << image.channels() << std::endl;

  u_char* hwc_data = image.data;
  std::vector<float> chw_data(height * width * channels);

  /* Convert HWC to CHW */
  int count=0;
  for (int c = 0; c < channels; ++c) {
    for (int h = 0; h < height; ++h) {
      for (int w = 0; w < width; ++w) {
        int srcIdx = h * width * channels + w * channels + c;
        int dstIdx = c * height * width + h * width + w;
        chw_data[dstIdx] = hwc_data[srcIdx] ;
      }
    }
  }

  return py::cast(chw_data);
}

PYBIND11_MODULE(cv_example, m) {
    m.def("hwc2chw", &hwc2chw, "A function which convert HWC to CHW");
}
