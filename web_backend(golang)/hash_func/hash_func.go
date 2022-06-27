package hash_func

import (
	"math"
	"strconv"
)

func To_hash(x string) (st string){
	for j:=0; j < len(x); j++{
		chisl := float64(x[j])
		tmp := int(math.Sqrt(chisl))
		st = st + strconv.Itoa(tmp)
   }
	return st
}
