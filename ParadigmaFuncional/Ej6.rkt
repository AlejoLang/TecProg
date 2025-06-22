#lang racket
(let ((x 9))
    ( * x 
        (let ((x (/ x 3)))
            (+ x x))))