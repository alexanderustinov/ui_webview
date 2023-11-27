## webview
При сборке на win с использованием MSYS2 нужно получить
WebView2 через nupkg (это можно сделать через использование
webview\script\build.sh) 

После этого можно
```
# нужны mingw-w64-x86_64-ninja mingw-w64-x86_64-gcc mingw-w64-x86_64-cmake в MSYS2
# или libgtk-3-dev libwebkit2gtk-4.0-dev в debian-based
mkdir build
cd build
cmake ../
ninja
```

Дополнительно про зависимости и про сборку на других платформах см. текст в
https://github.com/webview/webview