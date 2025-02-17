section .data
    triangle db '   *   ', 0
    radius dw 10 ; Радіус кола
    angle dw 0 ; Кут повороту
    x dw 0 ; Координата x центра кола
    y dw 10 ; Координата y центра кола
    
section .text
    global _start

_start:
    mov ax, 0x03 ; Встановити режим тексту 80x25
    int 0x10

    mov cx, 100 ; Кількість ітерацій
    mov bx, 0 ; Лічильник ітерацій
    
loop_start:
    ; Обчислення координат вершин трикутника
    mov ax, radius
    mul word [angle] ; ax = radius * angle
    mov dx, ax
    mov ax, radius
    mov bx, dx
    div word [angle] ; bx = radius * angle / 256 (приблизно)
    
    ; Виведення трикутника
    mov ax, [y]
    add ax, bx ; y-координата верхньої вершини
    mov dh, al
    mov ax, [x]
    add ax, dx ; x-координата верхньої вершини
    mov dl, al
    mov ah, 0x02 ; Вивести символ
    mov bh, 0 ; Сторінка
    mov bl, 0x07 ; Колір
    int 0x10
    
    mov ax, [y]
    add ax, bx ; y-координата нижньої вершини
    mov dh, al
    mov ax, [x]
    sub ax, dx ; x-координата нижньої вершини
    mov dl, al
    mov ah, 0x02
    mov bh, 0
    mov bl, 0x07
    int 0x10
    
    mov ax, [y]
    sub ax, bx ; y-координата середньої вершини
    mov dh, al
    mov ax, [x]
    mov dl, al
    mov ah, 0x02
    mov bh, 0
    mov bl, 0x07
    int 0x10
    
    ; Очищення попереднього трикутника
    mov ax, [y]
    add ax, bx ; y-координата верхньої вершини
    mov dh, al
    mov ax, [x]
    add ax, dx ; x-координата верхньої вершини
    mov dl, al
    mov ah, 0x09 ; Вивести пробіл
    mov bh, 0
    mov bl, 0x00 ; Чорний колір
    int 0x10
    
    mov ax, [y]
    add ax, bx ; y-координата нижньої вершини
    mov dh, al
    mov ax, [x]
    sub ax, dx ; x-координата нижньої вершини
    mov dl, al
    mov ah, 0x09
    mov bh, 0
    mov bl, 0x00
    int 0x10
    
    mov ax, [y]
    sub ax, bx ; y-координата середньої вершини
    mov dh, al
    mov ax, [x]
    mov dl, al
    mov ah, 0x09
    mov bh, 0
    mov bl, 0x00
    int 0x10
    
    ; Збільшення кута повороту
    inc word [angle]
    
    ; Затримка
    mov ax, 0x1000
    mov cx, 0x1000
    delay:
        dec cx
        jnz delay

    inc bx
    cmp bx, cx
    jl loop_start

    ; Завершення програми
    mov ax, 0x4c00
    int 0x21
