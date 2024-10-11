+++
title = '第二章-开始Golang学习'
date = 2024-10-11T22:11:37+08:00
draft = true
+++
# 1. 环境安装

安装Go语言环境在Windows，Linux和Mac上的步骤略有不同。以下是各个操作系统的安装过程：

要配置Go语言环境的特定版本（例如1.19），你需要执行以下步骤：

1. 首先，确保已经安装了Go语言环境。你可以通过在终端中运行以下命令来验证安装：

```
go version
```

如果能够显示已安装的Go版本，则说明安装成功。

2. 访问Go官方网站（https://golang.org/dl/），并下载所需版本的Go安装程序或安装包。选择与你的操作系统和架构相对应的版本。
3. 安装所下载的Go版本。根据你的操作系统，有以下几种安装方法：

- **Windows**: 双击下载的安装程序并按照提示完成安装过程。默认情况下，Go将安装在`C:\Go`目录下。
- **Linux**: 解压下载的安装包到你选择的目录。例如，可以将其解压到`/usr/local`目录下：

```
tar -C /usr/local -xzf go1.19.linux-amd64.tar.gz
```

注意将`go1.19.linux-amd64.tar.gz`替换成你下载的安装包的实际文件名。

- **Mac**: 双击下载的安装包并按照提示完成安装过程。默认情况下，Go将安装在`/usr/local/go`目录下。

4. 现在，你需要使用环境变量来设置Go的版本和路径。打开你的终端，并执行以下命令：

- **Windows**: 在`系统属性 -> 高级 -> 环境变量`中，添加一个名为`GOROOT`的变量，并将其值设置为Go的安装路径（例如`C:\Go`）。然后，在`Path`变量中添加`%GOROOT%\bin`。
- **Linux和Mac**: 使用文本编辑器打开你的`~/.profile`文件或者`~/.bashrc`文件，并添加以下内容：

```
export GOROOT=/usr/local/go
export PATH=$PATH:$GOROOT/bin
```

或者，如果你使用的是Zsh终端，请修改命令为：

5. 保存并关闭文件，然后在终端中执行以下命令使配置生效：

- **Windows**: 关闭并重新打开终端。
- **Linux和Mac**: 在终端中执行以下命令：

```
source ~/.profile
```

或者

6. 最后，使用以下命令验证Go的版本和安装是否正确：

```
go version
```

如果能够显示你安装的Go版本（例如go1.19），则说明配置成功。

现在，你已经成功配置了Go语言环境的特定版本（1.19），可以开始使用它进行开发了。记得设置好Go的工作路径（GOPATH）和选择一个集成开发环境（IDE）或者文本编辑器进行编码，这里使用Goland。

![](https://cdn.nlark.com/yuque/0/2023/png/25959274/1688871509809-1ed7d9ed-8057-4b28-9b8a-4d4655fd15d9.png)

# 2. 编码

## 2.1 准备工作

新建一个项目，结构如下

![](https://cdn.nlark.com/yuque/0/2023/png/25959274/1688871832425-40e02586-a2ca-4f6d-8433-f1a0fc629ffc.png)

## 2.2 编码

```
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

完成以后，在控制台输入指令

```
cd src/ch1/main/
go run hello_world.go
```

显示结果

```
Hello, World!
```

如果编译源码，需要另一个指令

```
go build hello_world.go
```

执行后，可以看到一个可执行程式

```
main > ll
total 3784
-rwxr-xr-x@ 1 jeholppx  staff   1.8M Jul  9 11:10 hello_world
-rw-r--r--@ 1 jeholppx  staff    74B Jul  9 11:05 hello_world.go
```

只要执行这个`hello_world`就可以打印上面的结果

## 2.3 基本程序结构

```
package main // 包，表明代码所在的模块（包）

import "fmt" // 引入代码的依赖

// 功能实现
func main() {
    fmt.Println("Hello, World!")
}
```

## 2.4 应用程序入口的标准

例程中helloworld是应用程序的入口，作为入口，有以下的基本要求

- 必须是main包/模块，声明为`package main`，目录名不一定为`main`
- 必须是main方法 `func main()`
- 文件名不一定写`main.go`，也可以是其他名字

### 2.4.1 实验

新建一个文件夹，拷贝源码，并执行`go run`

```
# 回到上一级目录
cd ..
# 新建一个hello的文件夹
mkdir hello
# 复制2.2的源码
cp ./main/hello_world.go ./hello/hello_world.go
# 切换文件夹并执行源码
cd ./hello
go run hello_world.go
```

运行结果如下

```
Hello, World!
```

如果修改源码

```
package main1 // before is main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

重新运行编译就会提示

```
package command-line-arguments is not a main package
```

## 2.5 main函数与其他编程语言的差异

### 2.5.1 返回值方面

C(++)/Java中：有指定的返回值

Go语言中

- `main()`不支持任何返回值
- 通过`os.Exit`来返回状态

加返回值实验如下

```
package main

import "fmt"

func main() int {
    fmt.Println("Hello, World!")
    return 0
}
```

```
go run hello_world.go
# command-line-arguments
./hello_world.go:5:6: func main must have no arguments and no return values
```

若要返回状态，操作方法如下

```
package main

import (
    "fmt"
    "os"
)

func main() {
    fmt.Println("Hello, World!")
    os.Exit(0) // 返回值
}
```

这样又可以正常运行了

当然，返回值也可以定义为一个异常值，如-1

```
package main

import (
    "fmt"
    "os"
)

func main() {
    fmt.Println("Hello, World!")
    os.Exit(-1) // 异常返回
}
```

运行结果如下

```
Hello, World!
exit status 255 # 异常状态
```

### 2.5.2 传参方面

C++/Java 可以在main函数传参，args string[] 类型

Go不可以这样做

- `main()`本身就不支持传参
- 需要通过`os.Args()`获取参数

程序实例如下

```
package main

import (
    "fmt"
    "os"
)

func main() {
    args := os.Args
    fmt.Println("Hello, World!")
    fmt.Println(args)
    os.Exit(0)
}
```

```
> go run hello_world.go
Hello, World!
[/var/folders/s5/lh51989j3qv9nrz2p9tdjc8h0000gn/T/go-build3482274569/b001/exe/hello_world]
```

```
> go run hello_world.go chao
Hello, World!
[/var/folders/s5/lh51989j3qv9nrz2p9tdjc8h0000gn/T/go-build2433158551/b001/exe/hello_world chao]
```

第二个例子

```
package main

import (
    "fmt"
    "os"
)

func main() {
    if len(os.Args) > 1 {
        fmt.Println("Hello, World!", os.Args[1])
    }
}
```

```
> go run hello_world.go ppx
Hello, World! ppx
```