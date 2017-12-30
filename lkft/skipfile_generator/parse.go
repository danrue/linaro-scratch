package main

import (
	"fmt"
	"io/ioutil"
	"gopkg.in/yaml.v2"
	"os"
	"log"

)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

// Declare a custom StringArray type that can be used for parsing
// yaml fields that may be a string, or an array.
// See https://github.com/go-yaml/yaml/issues/100
type StringArray []string
func (a *StringArray) UnmarshalYAML(unmarshal func(interface{}) error) error {
	var multi []string
	err := unmarshal(&multi)
	if err != nil {
		var single string
		err := unmarshal(&single)
		if err != nil {
			return err
		}
		*a = []string{single}
	} else {
		*a = multi
	}
	return nil
}

func stringInSlice(a string, list []string) bool {
	for _, b := range list {
		if b == a || b == "all" {
			return true
		}
	}
	return false
}

// Structure of the yaml skipfile
type Skipfile struct {
	Matrix struct {
		Boards []string
		Branches []string
		Environments []string
	}
	Skiplist []struct {
		Reason string
		Url string
		Environments StringArray
		Boards StringArray
		Branches StringArray
		Tests []string
	}
}

func main() {

	buf, err := ioutil.ReadFile("skipfile.yaml")
	check(err)

	var skips Skipfile
	err = yaml.Unmarshal(buf, &skips)
	check(err)
	//fmt.Printf("%v\n", skips)

	for _, board := range skips.Matrix.Boards {
		for _, branch := range skips.Matrix.Branches {
			for _, environment := range skips.Matrix.Environments {
				skipfile := fmt.Sprintf("skiplist_%s_%s_%s", board, branch, environment)
				f, err := os.OpenFile(skipfile, os.O_RDWR|os.O_CREATE, 0644)
				if err != nil {
					log.Fatal(err)
				}
				for _, skip := range skips.Skiplist {
					if stringInSlice(board, skip.Boards) &&
					   stringInSlice(branch, skip.Branches) &&
					   stringInSlice(environment, skip.Environments) {
						for _, test := range skip.Tests {
							f.WriteString(fmt.Sprintf("%s\n", test))
						}
					}
				}
				if err := f.Close(); err != nil {
					log.Fatal(err)
				}
			}
		}
	}
}
