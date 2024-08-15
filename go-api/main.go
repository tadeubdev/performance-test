package main

import (
    "fmt"
    "log"
    "net/http"
)

func helloHandler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello from Go!")
}

func main() {
    http.HandleFunc("/", helloHandler)
    fmt.Println("Go server running on port 8081")
    log.Fatal(http.ListenAndServe(":8081", nil))
}