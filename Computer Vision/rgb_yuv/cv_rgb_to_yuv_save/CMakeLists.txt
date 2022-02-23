cmake_minimum_required(VERSION 3.4)
project(rgb_yuv_example)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSION OFF)

find_package(OpenCV REQUIRED)

# Source files
FILE(GLOB_RECURSE SOURCE_FILES
    "${CMAKE_SOURCE_DIR}/src/*.cpp"
    "${CMAKE_SOURCE_DIR}/src/*.cc"
    "${CMAKE_SOURCE_DIR}/src/*.c"
)

add_definitions(-DFLUID_LOCAL)
# Tell CMake to create the xxx executable
add_executable(${PROJECT_NAME} ${SOURCE_FILES})

target_link_libraries(${PROJECT_NAME} PRIVATE
    ${OpenCV_LIBS}
)
