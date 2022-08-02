package code

import (
	"reflect"
	"testing"
)

func Test_twoSum(t *testing.T) {
	type args struct {
		nums   []int
		target int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		// TODO: Add test cases.
		{
			name: "01",
			args: args{
				nums:   []int{3, 3},
				target: 6,
			},
			want: []int{0, 1},
		},
		{
			name: "02",
			args: args{
				nums:   []int{2, 7, 11, 15},
				target: 9,
			},
			want: []int{0, 1},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := twoSum(tt.args.nums, tt.args.target); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("twoSum() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_twoSumList(t *testing.T) {
	type args struct {
		nums   []int
		target int
	}
	tests := []struct {
		name string
		args args
		want [][]int
	}{
		{
			name: "01",
			args: args{
				nums:   []int{2, 7, 11, 15},
				target: 9,
			},
			want: [][]int{
				{2, 7},
			},
		},
		{
			name: "02",
			args: args{
				nums:   []int{2, 7, 11, 15},
				target: 13,
			},
			want: [][]int{
				{2, 11},
			},
		},
		{
			name: "02",
			args: args{
				nums:   []int{2, 4, 3, 3, 11, 15},
				target: 6,
			},
			want: [][]int{
				{2, 4},
				{3, 3},
			},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := twoSumList(tt.args.nums, tt.args.target); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("twoSumList() = %v, want %v", got, tt.want)
			}
		})
	}
}
