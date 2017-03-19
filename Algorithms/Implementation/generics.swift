import Foundation

struct Printer<T> {
	/**
	*    Name: printArray
	*    Print each element of the generic array on a new line. Do not return anything.
	*    @param A generic array
	**/
	func printArray<T: Sequence>(array: T) {
        for element in array {
          print(element)
        }
    }

}


var n = Int(readLine()!)!
var intArray = Array(repeating: 0, count: n);
for i in 0...n - 1 {
	intArray[i] = Int(readLine()!)!;
}

n = Int(readLine()!)!
var stringArray = Array(repeating: "", count: n);
for i in 0...n - 1 {
	stringArray[i] = readLine()!;
}

// var intArray = [1, 2, 3, 4, 5]
// var stringArray = ["a", "b", "c", "d'"]

Printer<Int>().printArray(array: intArray)
Printer<String>().printArray(array: stringArray)
