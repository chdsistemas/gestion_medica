# def inicio(request):
#     tipo_usuario = None

#     if request.user.is_authenticated:
#         usuario_logueado = request.user
#         if isinstance(usuario_logueado, Medico):
#             tipo_usuario = 'Medico'
#         elif isinstance(usuario_logueado, Paciente):
#             tipo_usuario = 'Paciente'
#         else:
#             tipo_usuario = 'Usuario no identificado'

#     return render(request, 'inicio.html', {'tipo_usuario': tipo_usuario})

