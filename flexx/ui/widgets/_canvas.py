"""
"""

from ... import event
from ...pyscript import window
from .. import Widget


class CanvasWidget(Widget):
    """ A widget that provides an HTML5 canvas. The canvas is scaled with
    the available space.
    """
    
    CSS = """
    .flx-CanvasWidget {
        min-width: 50px;
        min-height: 50px;
    }
    """ 
    
    class JS:
        
        def init(self):
            
            self.p = window.phosphor.createWidget('div')
            self.canvas = window.document.createElement('canvas')
            self.p.node.appendChild(self.canvas)
            # Set position to absolute so that the canvas is not going
            # to be forcing a size on the container div.
            self.canvas.style.position = 'absolute'
            
            # _mouse_down = lambda ev: self.mouse_down._set(1)
            # _mouse_up = lambda ev: self.mouse_down._set(0)
            # _mouse_move = lambda ev: self.mouse_pos._set((ev.clientX, ev.clientY))
            # self.canvas.addEventListener('mousedown', _mouse_down, 0)
            # self.canvas.addEventListener('mouseup', _mouse_up, 0)
            # self.canvas.addEventListener('mousemove', _mouse_move, 0)
        
        @event.connect('size')
        def _update_canvas_size(self, *events):
            size = events[-1].new_value
            if size[0] or size[1]:
                self.canvas.width = size[0]
                self.canvas.height = size[1]
                self.canvas.style.width = size[0] + 'px'
                self.canvas.style.height = size[1] + 'px'
        
        # todo: handle in widget???
        @event.emitter
        def mouse_down(v=False):
            """ True when the mouse is currently pressed down.
            """
            return {}
        
        @event.emitter
        def mouse_move(self, pos=(0, 0)):
            """ The current position of the mouse inside this widget.
            """
            return {}
            rect = self.canvas.getBoundingClientRect()
            offset = rect.left, rect.top
            return float(pos[0] - offset[0]), float(pos[1] - offset[1])
