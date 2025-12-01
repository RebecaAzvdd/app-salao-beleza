from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Agendamento
# Create your views here.
def home(request):
    produtos = Produto.objects.all()
    return render(request, "home.html", {"produtos": produtos})

def produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    return render(request, "produto.html", {"produto": produto})

def agendar(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == "POST":
        nome = request.POST["nome"]
        telefone = request.POST["telefone"]
        data = request.POST["data"]
        hora = request.POST["hora"]

        agenda = Agendamento.objects.create(
            nome_cliente=nome,
            telefone=telefone,
            produto=produto,
            data=data,
            horario=hora
        )

        mensagem = (
            f"Olá, gostaria de agendar:\n"
            f"🧖 Serviço: {produto.nome}\n"
            f"📅 Data: {data}\n"
            f"⏰ Horário: {hora}\n"
            f"👤 Cliente: {nome}\n"
            f"📞 Telefone: {telefone}"
        )

        url = f"https://wa.me/558199999999?text={mensagem.replace(' ', '%20')}"

        return redirect(url)

    return render(request, "agendar.html", {"produto": produto})