package main

import "fmt"

func main()  {
	hello()
	fmt.Println(add(10, 20, 1))
}

func hello()  {
	fmt.Println("Hello mundo")
//	fmt.Println("Hello mundo")
}

func add(x, y, u int) int{
	return x * y - u
}