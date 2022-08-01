package container

import (
	"fmt"
	"golang.org/x/exp/constraints"
)

func min[T constraints.Ordered](a, b T) T {
	if a < b {
		return a
	} else {
		return b
	}
}

func iMin[T INumber](a, b T) T {
	if a < b {
		return a
	} else {
		return b
	}
}

//func Scale[E constraints.Integer](s []E, c E) []E {
//	r := make([]E, len(s))
//	for i, v := range s {
//		r[i] = v * c
//	}
//	return r
//}

func Scale[S ~[]E, E constraints.Integer](s S, c E) S {
	r := make(S, len(s))
	for i, v := range s {
		r[i] = v * c
	}
	return r
}

type Point []int32

func (p Point) String() string {
	// 实现细节不重要，忽略
	return "point"
}

func ScaleAndPrint(p Point) {
	r := Scale(p, 2)
	fmt.Println(r.String())
}

type IMax interface {
	max()
}

type CInt int

func (c CInt) max() {

}

func fmax(m IMax) {

}