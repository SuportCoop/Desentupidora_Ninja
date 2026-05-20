async function BuscarCNPJ() {

    try {

        const campo = document.getElementById('id_documento');

        const cnpj = campo.value.replace(/\D/g, '');

        const response = await fetch(`/buscar-cnpj/${cnpj}/`);

        const dados = await response.json();

        console.log(dados);

    } catch (error) {

        console.error(error);

    }
}