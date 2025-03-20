from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'usuario'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(250), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(250), nullable=False)
    nombre: Mapped[str] = mapped_column(String(250), nullable=False)
    apellido: Mapped[str] = mapped_column(String(250), nullable=False)
    suscripcion: Mapped[int] = mapped_column(DateTime(), nullable=False)
    estado_activo: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "suscripcion": self.suscripcion.isoformat(),
            "estado_activo": self.estado_activo
        }

    # Relaciones
    usuario_favorito = relationship("favorito", back_populates="usuario")


class Personaje(db.Model):
    __tablename__ = 'personaje'

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre_personaje: Mapped[str] = mapped_column(String(250), nullable=False)
    altura: Mapped[float] = mapped_column(nullable=False)
    peso: Mapped[float] = mapped_column(nullable=False)
    color_pelo: Mapped[str] = mapped_column(String(100), nullable=False)
    color_piel: Mapped[str] = mapped_column(String(100), nullable=False)
    color_ojos: Mapped[str] = mapped_column(String(100), nullable=False)
    fecha_nacimiento: Mapped[str] = mapped_column(String(100), nullable=False)
    genero: Mapped[str] = mapped_column(String(100), nullable=False)
    especie: Mapped[str] = mapped_column(String(100), nullable=False)
    planeta_natal: Mapped[str] = mapped_column(String(100), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "nombre_personaje": self.nombre_personaje,
            "altura": self.altura,
            "peso": self.peso,
            "color_pelo": self.color_pelo,
            "color_piel": self.color_piel,
            "color_ojos": self.color_ojos,
            "fecha_nacimiento": self.fecha_nacimiento,
            "genero": self.genero,
            "especie": self.especie,
            "planeta_natal": self.planeta_natal
        }

    # Relaciones
    personaje_favorito = relationship("favorito", back_populates="personaje")


class Planeta(db.Model):
    __tablename__ = 'planeta'

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre_planeta: Mapped[str] = mapped_column(String(250), nullable=False)
    diametro: Mapped[float] = mapped_column(nullable=False)
    clima: Mapped[str] = mapped_column(String(100), nullable=False)
    poblacion: Mapped[int] = mapped_column(nullable=False)
    gravedad: Mapped[float] = mapped_column(nullable=False)
    periodo_rotacion: Mapped[float] = mapped_column(nullable=False)
    periodo_orbital: Mapped[float] = mapped_column(nullable=False)
    terreno: Mapped[str] = mapped_column(String(100), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "nombre_planeta": self.nombre_planeta,
            "diametro": self.diametro,
            "clima": self.clima,
            "poblacion": self.poblacion,
            "gravedad": self.gravedad,
            "periodo_rotacion": self.periodo_rotacion,
            "periodo_orbital": self.periodo_orbital,
            "terreno": self.terreno
        }

    # Relaciones
    planeta_favorito = relationship("favorito", back_populates="planeta")


class Favorito(db.Model):
    __tablename__ = 'favorito'

    id: Mapped[int] = mapped_column(primary_key=True)
    usuario_id: Mapped[int] = mapped_column(db.ForeignKey('usuario.id'), nullable=True, unique=True)
    personaje_id: Mapped[int] = mapped_column(
        db.ForeignKey('personaje.id'), nullable=True, unique=True)
    planeta_id: Mapped[int] = mapped_column(db.ForeignKey(
        'planeta.id'), nullable=True, unique=True)  # puede ser nula

    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "personaje_id": self.personaje_id,
            "planeta_id": self.planeta_id
        }