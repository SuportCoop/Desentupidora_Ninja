async function BuscarCNPJ() {

    const url = document.getElementById('CNPJ').value;
    const cnpjSemFormato = url.replace(/\D/g, '');
    const apiUrl = `https://open.cnpja.com/office/${cnpjSemFormato}`;


    await fetch(apiUrl).then((response) => {
        // Transforma JSON em OBJ
        return response.json();

    }).then((response) => {

        // Testando
        // console.log(response.founded)
        // console.log(response.company.members[1].person.name);
         console.log(response.address.street +','+ response.address.number);


        // document.getElementById('number').value = response.taxId
        document.getElementById('name').value = response.company.name
        document.getElementById('founded').value = response.founded

        // Members
        document.getElementById('name0').value = response.company.members[0].person.name
        document.getElementById('cargo0').value = response.company.members[0].role.text
        document.getElementById('name1').value = response.company.members[1].person.name
        document.getElementById('cargo1').value = response.company.members[1].role.text
        //document.getElementById('name2').value = response.company.members[2].person.name
        //document.getElementById('cargo2').value = response.company.members[2].role.text
        
        //Adress
        document.getElementById('address').value = response.address.street +', '+ response.address.number
        document.getElementById('city').value = response.address.city
        document.getElementById('district').value = response.address.district
        document.getElementById('zip').value = response.address.zip
        document.getElementById('country').value = response.address.country.name

        // Contato
        document.getElementById('phone').value =`(${(response.phones[0].area)})` + response.phones[0].number
        document.getElementById('email').value =response.emails[0].address
        document.getElementById('site').value =response.emails[0].domain
    })

}
function aplicarMascaraCNPJ(campo) {
    // Remove caracteres que não são números
    let valor = campo.value.replace(/\D/g, '');
    
    // Adiciona os pontos, a barra e o traço no lugar correto
    valor = valor.replace(/^(\d{2})(\d)/, '$1.$2');       // Primeiro ponto
    valor = valor.replace(/^(\d{2})\.(\d{3})(\d)/, '$1.$2.$3'); // Segundo ponto
    valor = valor.replace(/\.(\d{3})(\d)/, '.$1/$2');     // Barra
    valor = valor.replace(/(\d{4})(\d)/, '$1-$2');        // Traço

    // Atualiza o campo com a máscara
    campo.value = valor;
}





