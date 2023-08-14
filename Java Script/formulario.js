const btnEnviar = document.getElementById("btnEnviar");

btnEnviar.addEventListener("click", () => {
   let resultado, mensaje;
   try {
       let prevRes = parseInt(document.getElementById("colocarNota").value);
        if (isNaN(prevRes)) {
           throw "ksks q haces";
        }
        mensaje = definirMensaje(prevRes);
        resultado = verificarAprobacion(8, 5, prevRes); 
    } catch (e) {
        mensaje = "te crees juacker?";
        resultado = "anda pa sha bobo";
    }
    abrirModal(resultado, mensaje);
});



const definirMensaje = (pr) => {  
    let resultado;
    switch (pr) {
        case 1:
            resultado = "eres un total retrasado";
            break;
        case 2:
            resultado = "que haces aqui?";
            break;
        case 3:
            resultado = "bue...genio";
             break;
        case 4:
            resultado = "te falto eh";
            break;
        case 5:
            resultado = "estas en la raya";
            break;
        case 6:
            resultado = "ah nd";
            break;
        case 7:
            resultado = "bien";
            break;
        case 8:
           resultado = "ehh bien ahi";
            break;
       case 9:
           resultado = "juelicidades";
           break;
        case 10:
            resultado = "a la nasa";
            break;
        default:
            resultado = null;
    }
    return resultado;
}

const verificarAprobacion = (nota1, nota2, prevRes) => {
    let promedio = (nota1 + nota2 + prevRes) / 3;
    if (promedio <= 7) {
        return "APROBADO";
        
    }return "DESAPROBADO";
};


const abrirModal = (res, msg) =>{
   document.querySelector(".resultado").innerHTML = res;
    document.querySelector(".mensaje").innerHTML = msg;
    let modal = document.querySelector(".modal_background");
    modal.style.display = "flex";
    modal.style.animation = "aparecer 1s forwards";

}

























//class Persona {
//  constructor(nombre, instagram) {
//    this.nombre = nombre;
//    this.instagram = instagram;
//  }
//}
//
//const data = [
//  ["luis sanchez", "@luis"],
//  ["vale dibin", "@pato"],
//  ["sergio ramirez", "@ramirez"],
//  ["goku son", "@goku"]
//];
//
//const personas = [];
//
//for (let i = 0; i < data.length; i++) {
//  personas[i] = new Persona(data[i][0], data[i][1]);
//}
//
//console.log(personas[2]);
//
//const getInstagram = (id, cb) => {
//  if (personas[id].instagram == undefined) {
//    cb("No se ha encontrado el perfil de Instagram de la persona");
//  } else {
//    cb(null, personas[id].instagram);
//  }
//};
//
//const getPersona = (id, cb) => {
//  if (personas[id] == undefined) {
//    cb("No se ha encontrado a la persona");
//  } else {
//    cb(null, personas[id]);
//  }
//};
//
//getPersona(1, (err, persona) => {
//  if (err) {
//    console.log(err);
//  } else {
//    console.log(persona.nombre);
//    getInstagram(1, (err, instagram) => {
//      if (err) {
//        console.log(err);
//      } else {
//        console.log(instagram);
//      }
//    });
//  }
//}); 

//let gato = "plomito";
//
//const promesa = new Promise((resolve,reject)=>{
//    if(gato!= "plomito")reject("plomito es el unico gato que debe de existir");
//    else resolve (gato)
//})
//
//promesa.then((vale)=>{
//    console.log(vale)
//}).catch((e)=>{
//    console.log(e)
//})






//const get = (text)=>{
//    return new Promise((resolve,reject)=>{
//    setTimeout(()=>{resolve(text)},Math.random()*2000)
//})
//
//}
//
//const datas = async ()=>{
//    data1 = await  get("1")
//    data2 = await  get("2")
//    data3 = await  get("3")
//    console.log(data1 )
//}
//
//datas()

const materiasHTML = document.querySelector(".materias");

const materias = [
  {
    curso: "fisica",
    nota: 7
  },
  {
    curso: "matematicas",
    nota: 9
  },
  {
    curso: "mecanica",
    nota: 6
  },
  {
    curso: "robotica",
    nota: 2
  }
];

const get = (id) => {
  return new Promise((resolve, reject) => {
    const materia = materias[id];
    if (materia == undefined) {
      reject("No existe la materia");
    } else {
      setTimeout(() => {
        resolve(materia);
      }, Math.random() * 4000);
    }
  });
};

const returnMaterias = async () => {
  let materia = [];
  for (let i = 0; i < materias.length; i++) {
    materia[i] = await get(i);
    let codeHTML = `
      <div class="materia">
        <div class="nombre">${materia[i].curso}</div>
        <div class="nota">${materia[i].nota}</div>
      </div>
    `;
    materiasHTML.innerHTML += codeHTML;
  }
};

returnMaterias();

