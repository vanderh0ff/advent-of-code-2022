package main

import (
	"container/heap"
	"fmt"
	"math"
	"os"
	"strings"
)

type position struct {
	x int
	y int
	z int
}

type node struct {
	location position
	parent   position
	f        float64
	g        float64
	h        float64
	index    int
}

type PriorityQueue []*node

func (pq PriorityQueue) Len() int {
	return len(pq)
}
func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i].f > pq[j].f
}
func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}
func (pq *PriorityQueue) Push(x any) {
	n := len(*pq)
	node := x.(*node)
	node.index = n
	*pq = append(*pq, node)
}
func (pq *PriorityQueue) Pop() any {
	old := *pq
	n := len(old)
	item := old[n-1]
	old[n-1] = nil
	item.index = -1
	*pq = old[0:n-1]
	return item
}
func (pq *PriorityQueue) update(node *node) {
	heap.Fix(pq, node.index)
}

func get_distance(a position, b position) float64 {
	return math.Sqrt(float64((b.z - a.z) ^ 2 + (b.x - a.x) ^ 2 + (b.y - a.y) ^ 2))
}


// g cost = distance from start
// h cost = distance from end
// f cost = g + h
// explore paths based on the lowest fcost

// there will be a set of nodes to be evaluated and a set of nodes that have been evaluated
//
// add start node to open
// loop
//   current = node in open with lowest fcost
//   add current to closed
// if current is end return node
// foreach neighbor of current
// if neighbor is not traversable or neightr is in closed skip to next neighbor
//
// if new path to neighbor is shorter or neighbor is not in open
//   set f of neighbor
//   set parent of neighbor to current
// if neighbor is not in open add neighbor to open

func get_cost(start position, node node, current node, target position) {
	g := get_distance(start, node.location)
	h := get_distance(target, node.location)
	f := g + h
	if node.f > f {
		node.f = f
		node.g = g
		node.h = h
		node.parent = current.location
	}
}

func get_path(start position, end position, height_map [][]int) int {
	path_length := 0
	return path_length
}

func get_moves(node node){
	if node.location.z + 1 >= heightmap[node.location.x + 1][node.location.y] {
	}
	node.location.x - 1, node.location.y
	node.location.x, node.location.y + 1
	node.location.x, node.location.y - 1
}

func main() {
	test_map := load_map("test.txt")
	map_lines := strings.Split(string(test_map), "\n")
	open_nodes := make(PriorityQueue, 100)
	closed := make([]node,100)
	height_map := [40][40]int{}
	start_position := position{x: 0, y: 0}
	end_position := position{x: 0, y: 0}
	for line_number := int(0); line_number < int(len(map_lines)); line_number++ {
		for char := int(0); char < int(len(map_lines[line_number])); char++ {
			height_map[line_number][char] = int(map_lines[line_number][char]) - int('a') + 1
			if string(map_lines[line_number][char]) == "S" {
				start_position = position{x: line_number, y: char, z: int(1)}
				height_map[line_number][char] = 1
			}
			if string(map_lines[line_number][char]) == "E" {
				end_position = position{x: line_number, y: char, z: int(26)}
				height_map[line_number][char] = 26
			}
		}
	}
	
	current := node{location: start_position, g:0, h:get_distance(start_position, end_position) }
	
	fmt.Printf("start %v end %v, distance %v \n heightmap \n\n %v \n", start_position, end_position, get_distance(start_position, end_position), height_map)

}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func load_map(map_location string) []byte {
	// get the data from the file and save it to an array for traversing
	dat, err := os.ReadFile(map_location)
	check(err)
	return dat
}

func write_solution(solution string, location string) {
	err := os.WriteFile(location, []byte(solution), 0644)
	check(err)
}

func get_map_size() {

}

