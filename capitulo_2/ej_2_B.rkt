#lang racket
;Ejercicio 2.B

;Bob's box
(define (attach-tag tag contents) (cons tag contents))
(define (type-tag datum) (car datum))
(define (contents datum) (cdr datum))

(define (bob-make-box x y w h)
    (attach-tag 'bob-box
         (cons (cons x y) (cons w h))))

(define (bob-box? b) (eq? (type-tag b) 'bob-box))

(define (bob-width b) (car (cdr (contents b))))
(define (bob-height b) (cdr (cdr (contents b))))

(define (bob-area box)
    (* (bob-width box) (bob-height box)))

; Alice's box
(define (alice-make-box x1 y1 x2 y2)
  (attach-tag 'alice-box (cons (cons x1 y1) (cons x2 y2))))

(define (alice-box? b) (eq? (type-tag b) 'alice-box))

(define (alice-width b) (abs (- (car (cdr (contents b))) (car (car (contents b))))))
(define (alice-height b) (abs (- (cdr (cdr (contents b))) (cdr (car (contents b))))))

(define (alice-area box)
    (* (alice-width box) (alice-height box)))


(define a (alice-make-box 1 2 3 4))
(define b (bob-make-box 1 2 3 4))
(alice-area a)
(bob-area b)

a

b