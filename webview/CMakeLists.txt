cmake_minimum_required(VERSION 3.11)
project(ui_webview CXX)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON) 

# https://stackoverflow.com/q/77465466
if(APPLE)
        target_link_libraries(${PROJECT_NAME} "-framework WebKit")
    elseif (UNIX)
        find_package(PkgConfig REQUIRED)
        pkg_check_modules(GTK3 REQUIRED gtk+-3.0)
        pkg_check_modules(WEBKIT2GTK4 REQUIRED webkit2gtk-4.0)
        include_directories(${GTK3_INCLUDE_DIRS} ${WEBKIT2GTK4_INCLUDE_DIRS})
        target_link_libraries(${PROJECT_NAME} ${GTK3_LIBRARIES} ${WEBKIT2GTK4_LIBRARIES})
    elseif (MSVC)
        target_compile_options(${PROJECT_NAME} PRIVATE -mwindows -Ilibs/webview2/build/native/include -ladvapi32 -lole32 -lshell32 -lshlwapi -luser32 -lversion)
    endif()

include_directories( webview )

add_executable(ui_webview
    src/main.cpp
    webview/webview.cc
    )

target_link_libraries(ui_webview) 