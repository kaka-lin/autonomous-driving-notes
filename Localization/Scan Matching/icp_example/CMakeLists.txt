cmake_minimum_required (VERSION 3.10)
project(iterative_closest_point)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CXX_FLAGS "-pthread -fPIC")
set(CMAKE_CXX_FLAGS "${CXX_FLAGS}")

# Find PCL package
find_package(PCL 1.2 REQUIRED)

# Source files
#set(sources icp1-main.cpp helper.cpp)
FILE(GLOB_RECURSE SOURCE_FILES
    "${CMAKE_SOURCE_DIR}/src/*.cpp"
    "${CMAKE_SOURCE_DIR}/src/*.cc"
    "${CMAKE_SOURCE_DIR}/src/*.c"
)

include_directories(${PCL_INCLUDE_DIRS})
link_directories(${PCL_LIBRARY_DIRS})
add_definitions(${PCL_DEFINITIONS})

add_executable(${PROJECT_NAME} ${SOURCE_FILES})
target_link_libraries(${PROJECT_NAME} ${PCL_LIBRARIES})
