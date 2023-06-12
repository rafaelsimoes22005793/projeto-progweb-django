function modes(){

    var button = document.querySelector("#dmbtn");
    var div = document.getElementById("menu").style;
    var op1 = document.getElementById("op1").style;
    var op2 = document.getElementById("op2").style;
    var op4 = document.getElementById("op4").style;
    var op5 = document.getElementById("op5").style;
    var op6 = document.getElementById("op6").style;
    var op7 = document.getElementById("op7").style;
    var footer = document.getElementById("footer").style;
    var divFooter = document.getElementById("divFooter").style;


    if (button.className == "fa-regular fa-sun"){
        button.className = "fa-regular fa-moon";
        div.backgroundColor = "rgb(255,255,255)";
        button.style.color = "#000000";
        op1.color = "#000000";
        op2.color = "#000000";
        op4.color = "#000000";
        op5.color = "#000000";
        op6.color = "#000000";
        op7.color = "#000000";
        op8.color = "#000000";
        footer.backgroundColor = "rgb(255,255,255)";
        divFooter.backgroundColor = "rgb(255,255,255)";
        divFooter.color = "#000000";
        
    }
    else if (button.className = "fa-regular fa-moon"){
        button.className = "fa-regular fa-sun";
        div.backgroundColor = "rgb(51,51,51)"; 
        button.style.color = "#ffffff"; 
        op1.color = "#ffffff";
        op2.color = "#ffffff";
        op4.color = "#ffffff";
        op5.color = "#ffffff";
        op6.color = "#ffffff";
        op7.color = "#ffffff";
        op8.color = "#ffffff";
        footer.backgroundColor = "rgb(51,51,51)"; 
        divFooter.backgroundColor = "rgb(51,51,51)"; 
        divFooter.color = "#ffffff";
        
    }
    
    }


    function fazContas(e){

        var conta = document.getElementById("conta").value;
        var resultado = document.getElementById("resultado");
        var result = eval(conta);
        if (result == undefined){
            resultado.innerHTML = "0"
        } else {
            resultado.innerHTML = result;
        }

    }


    function limpar(e) {
        document.getElementById("conta").value = "";
        document.getElementById("resultado").innerHTML = "";
    }

    function limparNome(e) {
        document.getElementById("nome").value = "";
        document.getElementById("name1").innerHTML = "";
        document.getElementById("name2").innerHTML = "";
        document.getElementById("name3").innerHTML = "";
    }

    function submitName(e){

        var nome = document.getElementById("nome").value;
        var nomeDisplay1 = document.getElementById("name1");
        var nomeDisplay2 = document.getElementById("name2");
        var nomeDisplay3 = document.getElementById("name3");

        if (nome == ""){
            nomeDisplay2.innerHTML = "Insira um nome"
        } else {
            nomeDisplay1.innerHTML = nome;
            nomeDisplay2.innerHTML = nome;
            nomeDisplay3.innerHTML = nome;
        }

    }

    function mouseOver(e){
        var texto = document.getElementById("js").style;
        texto.color = "rgb(255,140,0)";

    }

    function mouseOut(e){
        var texto = document.getElementById("js").style;
        texto.color = "rgb(255,255,255)";

    }

    function inserirData(e){
        var dataHTML = document.getElementById("todayDate");
        const date = new Date();
        const meses =new Array ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho",
         "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro");
        var dia = date.getDate();
        var mes = date.getMonth();
        var ano = date.getFullYear();
        dataHTML.innerHTML = dia + " de " + meses[mes] + ", " + ano;
    }