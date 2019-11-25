#!/bin/bash
curl -X POST http://localhost:5000/shutdown | xargs echo > deadclient
