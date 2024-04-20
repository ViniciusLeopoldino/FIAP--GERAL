document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('cadastro');

  form.addEventListener('submit', function (e) {
    e.preventDefault();

    // Obter os valores dos campos de entrada
    const nome = document.getElementById('nome').value;
    const veiculo = document.getElementById('Veiculo').value;
    const ano = document.getElementById('Ano').value;
    const modelo = document.getElementById('Modelo').value;
    const placa = document.getElementById('Placa').value;

    // Criar um objeto com os dados do registro
    const registro = {
      nome: nome,
      veiculo: veiculo,
      ano: ano,
      modelo: modelo,
      placa: placa
    };

    // Verificar se já existem registros no localStorage
    let registros = localStorage.getItem('registros');
    if (!registros) {
      registros = []; // Se não houver registros, inicialize com um array vazio
    } else {
      registros = JSON.parse(registros); // Se houver registros, parse como um array
    }

    // Adicionar o novo registro ao array
    registros.push(registro);

    // Salvar o array atualizado de registros de volta no localStorage
    localStorage.setItem('registros', JSON.stringify(registros));

    alert('Registro salvo com sucesso!');

    // Redirecionar para a página de login após o registro bem-sucedido
    window.location.href = 'login.html';

  });
});


