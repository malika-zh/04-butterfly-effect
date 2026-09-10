import taichi as ti

ti.init(arch=ti.gpu)


@ti.data_oriented
class ButterflyChaosEngine:

  def __init__(self, num_particles: int = 1_000_000):
    self.num_particles = num_particles
    self.pos = ti.field(dtype=ti.math.vec3, shape=(num_particles,))

    self.sigma = 10.0
    self.rho = 28.0
    self.beta = 8.0 / 3.0

    self.init_particles()

  @ti.kernel
  def init_particles(self):
    for i in self.pos:
      self.pos[i] = ti.math.vec3(
          ti.random() * 2.0 - 1.0 + 0.01,
          ti.random() * 2.0 - 1.0,
          ti.random() * 2.0 - 1.0 + 25.0,
      )

  @ti.kernel
  def update(self, dt: float):
    for i in self.pos:
      p = self.pos[i]
      x, y, z = p[0], p[1], p[2]

      dx = self.sigma * (y - x)
      dy = x * (self.rho - z) - y
      dz = x * y - self.beta * z

      x += dx * dt
      y += dy * dt
      z += dz * dt

      self.pos[i] = ti.math.vec3(x, y, z)