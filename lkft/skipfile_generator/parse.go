package main

import (
	"fmt"
	"io/ioutil"
	"gopkg.in/yaml.v2"

)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

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

type Skipfile struct {
	Matrix struct {
		Environments []string
		Boards []string
		Branches []string
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
	fmt.Printf("%v\n", skips)


}
