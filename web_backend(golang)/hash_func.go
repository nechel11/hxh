package main

import (
	"math"
	"strconv"
)

func hash_func(x string) (st string){
	for j:=0; j < len(x); j++{
		chisl := float64(x[j])
		tmp := int(math.Sqrt(chisl))
		st = st + strconv.Itoa(tmp)
   }
	return st
}
