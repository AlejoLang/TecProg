#lang racket
(define (distance2d x y)
    (let ((dx (- (car x) (car y)))
           (dy (- (cdr x) (cdr y))))
        (sqrt (+ (* dx dx) (* dy dy))) 
    )
)

(distance2d '(1 . 1) '(2 . 2))