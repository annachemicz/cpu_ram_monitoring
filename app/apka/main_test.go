package main

import "testing"

func TestExample(t *testing.T) {
	expected := 2 + 2
	if expected != 4 {
		t.Errorf("Expected 4, got %d", expected)
	}
}

