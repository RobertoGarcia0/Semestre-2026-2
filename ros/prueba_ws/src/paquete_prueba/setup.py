from setuptools import find_packages, setup

package_name = 'paquete_prueba'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ["launch/launch_prueba.launch.py"]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='robotics',
    maintainer_email='roberto.gar.1748@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
          "programa_publicador = paquete_prueba.publicador:main",
          "programa_suscriptor = paquete_prueba.suscriptor:main",
          "programa_cliente  = paquete_prueba.cliente:main",
          "programa_servidor = paquete_prueba.servidor:main",
          "programa_accion_cliente  = paquete_prueba.cliente_accion:main",
          "programa_accion_servidor = paquete_prueba.servidor_accion:main"
        ],
    },
)
