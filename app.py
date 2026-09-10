import taichi as ti
from chaos_gpu import ButterflyChaosEngine


def main():
  width, height = 1000, 1000
  
  engine = ButterflyChaosEngine(num_particles=1_000_000)

  window = ti.ui.Window(
      'GPU Butterfly Effect & Chaos Simulation', (width, height)
  )
  canvas = window.get_canvas()
  scene = window.get_scene()
  camera = ti.ui.Camera()


  camera.position(0.0, -80.0, 30.0)
  camera.lookat(0.0, 0.0, 25.0)

  print('Chaos Attractor Initialized. Rendering 1,000,000 particles on GPU...')

  while window.running:
    
    camera.track_user_inputs(window, movement_speed=2.0, hold_key=ti.ui.RMB)

    
    for _ in range(3):
      engine.update(0.004)

    scene.set_camera(camera)
    scene.ambient_light((0.2, 0.2, 0.2))

    
    scene.particles(engine.pos, radius=0.08, color=(0.0, 0.9, 1.0))

    canvas.scene(scene)
    window.show()


if __name__ == '__main__':
  main()