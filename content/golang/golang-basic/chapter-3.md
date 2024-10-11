+++
title = '第三章-变量、常量类型及使用技巧'
date = 2024-10-11T22:13:38+08:00
draft = false
+++

# 0.课前作业

## 编写一个测试程序

要求如下

1. 源码文件以 `_test`结尾：`xxx_test.go`
2. 测试方法名以 `Test`开头

```
func TestXXX(t *testing.T) {
    // ... here is your code
}
```

样例代码

```
package try_test

import "testing"

func TestFirstTry(t *testing.T) {
    t.Log("My first try!")
}
```

# Go语言赋值(变量定义)特点

与其它主要编程语言差异

- 赋值可以自动进行类型推断
- 在一个赋值语句中可以对多个变量进行同时赋值

```
package fib

import (
    "fmt"
    "testing"
)

func TestFibTest(t *testing.T) {
    // 第一种赋值方法
    //var a int = 1
    //var b int = 1
    // 第二种
    //var (
    //    a int = 1
    //    b  = 1
    //)
    // 第三种（推荐）
    //a := 1
    //b := 1
    // 假如函数返回值有多个，可以使用
    a, b := 1, 1
    t.Log(a)
    for i := 0; i < 5; i++ {
        t.Log(b)
        tmp := a
        a = b
        b = tmp + a
    }
    fmt.Println()
}
```

测试结果

```
GOROOT=/usr/local/go #gosetup
GOPATH=/Users/jeholppx/go #gosetup
/usr/local/go/bin/go test -c -o /Users/jeholppx/Library/Caches/JetBrains/GoLand2023.1/tmp/GoLand/___awesomeProject_src_ch2_fib__TestFibTest.test awesomeProject/src/ch2/fib #gosetup
/usr/local/go/bin/go tool test2json -t /Users/jeholppx/Library/Caches/JetBrains/GoLand2023.1/tmp/GoLand/___awesomeProject_src_ch2_fib__TestFibTest.test -test.v -test.paniconexit0 -test.run ^\QTestFibTest\E$
=== RUN   TestFibTest
    fib_test.go:18: 1
    fib_test.go:20: 1
    fib_test.go:20: 2
    fib_test.go:20: 3
    fib_test.go:20: 5
    fib_test.go:20: 8

--- PASS: TestFibTest (0.00s)
PASS
```

样例2

```
// 包名、引入均省略
func TestExchange(t *testing.T) {
    a := 1
    b := 2
    // 常规写法
    //tmp := a
    //a = b
    //b = tmp
    // 连续赋值写法
    a, b = b, a
    t.Log("a =", a, "b =", b)
}
```

输出结果

```
/usr/local/go/bin/go tool test2json -t /Users/jeholppx/Library/Caches/JetBrains/GoLand2023.1/tmp/GoLand/___awesomeProject_src_ch2_fib__TestExchange.test -test.v -test.paniconexit0 -test.run ^\QTestExchange\E$
=== RUN   TestExchange
    fib_test.go:36: a = 2 b = 1
--- PASS: TestExchange (0.00s)
PASS
```

# 常量的定义

## 快速设置连续的const值

常规连续值

```
package constant_test

import "testing"

// go 语言推荐的连续变量写法
const (
    Monday = iota + 1 // 1
    Tuesday // 2
    Wednesday // 3
)

// 也可以像其他语言那样去写
//const (
//    Monday = 1 // 1
//    Tuesday = 2 // 2
//    Wednesday = 3 // 3
//)

func TestConstantTry(t *testing.T) {
    t.Log(Monday, Tuesday)
}
```

测试结果

```
=== RUN   TestConstantTry
    constant_test.go:12: 1 2
--- PASS: TestConstantTry (0.00s)
PASS
```

## 定义一个连续位移，且参与逻辑运算的const值

```
// 声明包、导包略
// 连续位移写法
const (
    Readable   = 1 << iota // 001
    Writeable              // 010
    Executable             // 100
)

func TestConstantTry1(t *testing.T) {
    a := 7                                       // 111
    t.Log(a&Readable, a&Writeable, a&Executable) // 001 010 100
    t.Log("isReadable:", a&Readable == Readable)
    t.Log("isWriteable:", a&Writeable == Writeable)
    t.Log("isExecutable:", a&Executable == Executable)
}
```

运行结果

```
=== RUN   TestConstantTry1
    constant_test.go:21: 1 2 4
    constant_test.go:22: isReadable: true
    constant_test.go:23: isWriteable: true
    constant_test.go:24: isExecutable: true
--- PASS: TestConstantTry1 (0.00s)
PASS
```

# 基本数据类型

## 数据类型分类

常见的基本数据类型，可分为以下几类

- 布尔型：`bool`
- 字符型：`string`
- 整型：`int` `int8` `int16` `int32` `int64`
- 无符号整型：`uint` `uint8` `uint16` `uint32` `uint64` `uintptr`
- 字节型：`byte // alias for uint8`
- unicode编码值：`rune // alias for int32`
- 浮点型：`float32` `float64`
- 复数型：`complex64` `complex128`

## 差异

与其它主要编程语言的差异

1. ❌ Golang 不允许隐式类型转换
2. ❌ 别名与原有类型之间也不能进行隐式转换

错误案例1：隐式变量转换 int to int64

```
package type_test

import "testing"

func TestImplicit(t *testing.T) {
    var a int = 1
    var b int64
    b = a
    t.Log(a, b)
}
```

运行结果

```
# awesomeProject/src/ch3/type_test_test [awesomeProject/src/ch3/type_test.test]
./type_test.go:8:6: cannot use a (variable of type int) as type int64 in assignment
```

错误案例2：int32 to int64

```
package type_test

import "testing"

func TestImplicit(t *testing.T) {
    var a int32 = 1 // 差异点
    var b int64
    b = a // 修正方案：b = int64(a)
    t.Log(a, b)
}
```

运行结果

```
# awesomeProject/src/ch3/type_test_test [awesomeProject/src/ch3/type_test.test]
./type_test.go:8:6: cannot use a (variable of type int32) as type int64 in assignment
```

错误用例2修正后

```
// ignore package claim and import packages
func TestImplicit(t *testing.T) {
    var a int32 = 1
    var b int64
    b = int64(a)
    t.Log("a =", a, "b =", b)
}
```

改进后的错误用例2

```
=== RUN   TestImplicit
    type_test.go:11: a = 1 b = 1
--- PASS: TestImplicit (0.00s)
PASS
```

错误用例3：别名与原名类型间的转换

```
type MyInteger int64

func TestImplicit(t *testing.T) {
    var a int32 = 1
    var b int64
    b = int64(a)
    var c MyInteger
    c = b
    t.Log("a =", a, "b =", b, "c = ", c)
}
```

运行结果

```
# awesomeProject/src/ch3/type_test_test [awesomeProject/src/ch3/type_test.test]
./type_test.go:12:6: cannot use b (variable of type int64) as type MyInteger in assignment
```

改进方法

```
func TestImplicit(t *testing.T) {
    var a int32 = 1
    var b int64
    b = int64(a)
    var c MyInteger
    c = MyInteger(b) // 正解
    t.Log("a =", a, "b =", b, "c = ", c)
}
```

运行结果

```
=== RUN   TestImplicit
    type_test.go:13: a = 1 b = 1 c = 1
--- PASS: TestImplicit (0.00s)
PASS
```

# 预定义值

以下预定义值很常见，仅举几例

- `math.MaxInt64`
- `math.MaxFloat64`
- `math.MaxUint32`

# 指针类型

与C/C++不同的是

1. 不支持指针运算
2. `string`是值类型，其默认初始化值为空字符串，而不是 `nil`（go语言中, `null`其实是 `nil`）

样例1（正例）

```
func TestPoint(t *testing.T) {
    a := 1
    aPtr := &a
    t.Log("a =", a, "\nA's RAM address is", aPtr)
    t.Logf("a type is %T, aPtr type is %T", a, aPtr)
}
```

运行结果

```
=== RUN   TestPoint
type_test.go:19: a = 1 
A's RAM address is 0x1400010a1d8
type_test.go:20: a type is int, aPtr type is *int
--- PASS: TestPoint (0.00s)
PASS
```

到这里会以为和C/C++没什么两样，但是，这样做可以吗？

```
func TestPoint(t *testing.T) {
    a := 1
    aPtr := &a
    aPtr = aPtr + 1 // 请判断正误
    t.Log("a =", a, "\nA's RAM address is", aPtr)
    t.Logf("a type is %T, aPtr type is %T", a, aPtr)
}
```

在判断做法后，看下结果和你预想的是否一样

```
# awesomeProject/src/ch3/type_test_test [awesomeProject/src/ch3/type_test.test]
./type_test.go:19:16: cannot convert 1 (untyped int constant) to *int
```

用例2 字符串

```
func TestString(t *testing.T) {
    var s string
    t.Log("*" + s + "*")
    t.Log("Is var \"s\" an empty-string ?", s == "")
    t.Log("s longs:", len(s))
}
```

运行结果

```
=== RUN   TestString
    type_test.go:26: **
    type_test.go:27: Is var "s" an empty-string ? true
    type_test.go:28: s longs: 0
--- PASS: TestString (0.00s)
PASS
```

判断字符串为空，这样可以吗？

```
func TestString(t *testing.T) {
    var s string
    t.Log("*" + s + "*")
    t.Log("s longs:", len(s))
    // 这样判断可以吗？
    if s == nil {
        t.Log("s is empty")
    } else {
        t.Log("s is not empty")
    }
}
```

揭晓答案

```
# awesomeProject/src/ch3/type_test_test [awesomeProject/src/ch3/type_test.test]
./type_test.go:29:10: invalid operation: s == nil (mismatched types string and untyped nil)
```

显然这样做是错的，因为string的默认值为空字符串，因此不要这样做

正解如下：

```
func TestString(t *testing.T) {
    var s string
    t.Log("*" + s + "*")
    t.Log("s longs:", len(s))
    // 改进如下
    if s == "" {
        t.Log("s is empty")
    } else {
        t.Log("s is not empty")
    }
}
```

运行结果

```
=== RUN   TestString
        type_test.go:30: s is empty
--- PASS: TestString (0.00s)
PASS
```

# 小结和注意事项

- ❌：不允许隐式类型转换，尤其同一种类型的不同别名
- ❌：指针类型不可以参与任何运算
- ✅：判断字符串是某个值可以直接使用 `==`，不为空使用 `!=`
- ✅：判断字符串为空可以用 `str == ""`来表示
- ❌：不可以用 `str == nil`判空
