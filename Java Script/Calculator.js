class CALCULADORA {
    constructor() {}

    Calculadora(num1, num2) {
        return [parseFloat(num1), parseInt(num2)];
    }

    operacion(elegirOperacion, num1, num2) {
        if (elegirOperacion == 1) {
            return this.Calculadora(num1, num2)[0] + this.Calculadora(num1, num2)[1];
        } else if (elegirOperacion == 2) {
            return this.Calculadora(num1, num2)[0] - this.Calculadora(num1, num2)[1];
        } else if (elegirOperacion == 3) {
            return this.Calculadora(num1, num2)[0] * this.Calculadora(num1, num2)[1];
        } else if (elegirOperacion == 4) {
            return this.Calculadora(num1, num2)[0] / this.Calculadora(num1, num2)[1];
        } else if (elegirOperacion == 5){
            return this.Calculadora(num1, num2)[0] ** this.Calculadora(num1, num2)[1];
        }else if (elegirOperacion = 6){
            return Math.sqrt(this.Calculadora(num1)[0])
        }else {
            return "opción inválida";
        }
    }
}




let calculadora = new CALCULADORA();
let elegirOperacion = parseInt(prompt("Elige una operación (1: suma, 2: resta, 3: multiplicación, 4: división):"));
let num1 = parseFloat(prompt("Ingresa el primer número:"));
let num2 = parseInt(prompt("Ingresa el segundo número:"));
let resultado = calculadora.operacion(elegirOperacion, num1, num2);
alert(`El resultado es: ${resultado}`);
