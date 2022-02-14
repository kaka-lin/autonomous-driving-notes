cmake_minimum_required(VERSION 3.1)

project(cloud_viewer)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSION OFF)

# Find Qt location
# Please change this to your qt5 path
#list(APPEND CMAKE_PREFIX_PATH "/opt/Qt5")

# init_qt: Let's do the CMake job for us
set(CMAKE_AUTOMOC ON) # For meta object compiler
set(CMAKE_AUTORCC ON) # Resource files
set(CMAKE_AUTOUIC ON) # UI files

# Find includes in corresponding build directories
set(CMAKE_INCLUDE_CURRENT_DIR ON)

# Find the QtWidgets library
#find_package(Qt5 REQUIRED Widgets)
#find_package(VTK REQUIRED)
find_package(PCL 1.8 REQUIRED COMPONENTS common io visualization)

# Fix a compilation bug under ubuntu 16.04 (Xenial)
#list(REMOVE_ITEM PCL_LIBRARIES "vtkproj4")

# Source files
FILE(GLOB_RECURSE SOURCE_FILES
    "${CMAKE_SOURCE_DIR}/src/*.cpp"
    "${CMAKE_SOURCE_DIR}/src/*.c"
)

# [C/C++]>[General]>[Additional Include Directories]
include_directories( ${PCL_INCLUDE_DIRS} )
# [C/C++]>[Preprocessor]>[Preprocessor Definitions]
add_definitions( ${PCL_DEFINITIONS} )
# For Use Not PreCompiled Features
#add_definitions( -DPCL_NO_PRECOMPILE )
# [Linker]>[General]>[Additional Library Directories]
link_directories( ${PCL_LIBRARY_DIRS} )

add_executable(${PROJECT_NAME} ${SOURCE_FILES})

target_link_libraries(${PROJECT_NAME} ${PCL_LIBRARIES})

install(TARGETS ${PROJECT_NAME} DESTINATION bin)
