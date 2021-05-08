package main

import "fmt"

func main() {
	var input string
	_, err := fmt.Scanln(&input)
	if err != nil {
		panic(err)
	}

	fmt.Println(strings.atoi(input))

	/*if int(input) % 2 == 0
		fmt.Println("odd")
	else :
	fmt.Println("add")
	*/
	fmt.Println("Hello Goorm! Your input is", input)
}
