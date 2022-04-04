package main

import (
	"context"
	"fmt"
	"log"

	"github.com/ethereum/go-ethereum/ethclient"
)

func main() {
	client, err := ethclient.Dial("https://polygon-rpc.com")
	if err != nil {
		log.Fatalf("Problem: ", err)
	}
	fmt.Println("connected")
	ctx := context.Background()
	id, err := client.ChainID(ctx)
	if err != nil {
		log.Fatalf("Problem: ", err)
	}
	fmt.Println("Id: ", id)

	gas, err := client.SuggestGasPrice(ctx)
	if err != nil {
		log.Fatalf("Problem: ", err)
	}
	fmt.Println(gas)

	blockPointer, _ := client.BlockByNumber(ctx, nil)
	block := *blockPointer
	txns := block.Transactions()
	for _, val := range txns {
		fmt.Printf("%+v\n", val)
	}
}
