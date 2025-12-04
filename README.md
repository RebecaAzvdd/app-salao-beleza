# 🛍️ Sistema de Agendamentos com Múltiplos Produtos

Projeto Django que permite ao usuário selecionar o produtos, e finalizar um agendamento pedindo as informações do usúario e enviando para o whatsapp. Inclui listagem de produtos e organização de templates/static.

---

## 🚀 Funcionalidades

* Listagem e seleção de múltiplos produtos
* Criação de agendamento vinculado ao usuário
* Templates organizados + CSS dentro de `/static`

---

## 🧱 Estrutura Simplificada

```
core/
templates/
static/css/home.css
manage.py
```

---

## ⚙️ Como rodar

```bash
git clone <repo>
cd projeto
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 🎨 CSS nos templates

```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/home.css' %}">
```

---

## 👩‍💻 Autora

**Rebeca Pereira de Azevedo**
Projeto acadêmico para a cadeira de Desenvolvimento Web Backend.

---
