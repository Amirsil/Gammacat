#!/bin/bash
curl -X POST http://localhost:5555/shutdown | xargs echo > deadserver