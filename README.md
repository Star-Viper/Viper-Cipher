﻿# Viper Cipher
 
My own encryption decryption algorithm 

## Introduction

This repository contains my own encryption and decryption algorithm implemented in Python. The algorithm follows a series of steps to encrypt plaintext and decrypt ciphertext using a provided key.

## Encryption/Decryption Steps

1. **Input**: Take plaintext of capital letters and a key of numbers from 1 to 26.
2. **Shift**: Shift the plaintext characters according to the numerical value of the key.
3. **Reverse**: Reverse the shifted string.
4. **Matrix**: Put the reversed string in a matrix with 3 columns.
5. **Zigzag Reading**: Generate ciphertext by reading the matrix in zigzag order (left to right, right to left, repeat).

## Strengths

- **Customizable**: The algorithm allows users to choose a key value for encryption and decryption.
- **Simple Implementation**: The algorithm is implemented using basic string manipulation and matrix operations, making it easy to understand and implement.
- **Zigzag Reading**: Zigzag reading of the matrix enhances the security of the encryption.

## Weaknesses

- **Limited Character Set**: The algorithm only supports capital letters in plaintext. It does not support numbers, special characters, or lowercase letters.
- **Key Space**: As the key space is limited to numbers from 1 to 26, brute force attacks could be feasible if the key is not sufficiently random.
- **Vulnerability to Cryptanalysis**: The simplicity of the algorithm may make it vulnerable to certain cryptanalysis techniques, especially if the ciphertext is long enough for frequency analysis.
