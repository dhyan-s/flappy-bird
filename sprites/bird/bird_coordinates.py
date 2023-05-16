import pygame

class BirdCoordinates:
    """
    A helper class that simplifies accessing and modifying the coordinates of a bird object.

    Instead of directly accessing and modifying the coordinates through the bird's rectangle object,
    this class provides convenient attributes to access and modify individual coordinates.
    """
    
    def __init__(self, bird_rect: pygame.Rect):
        self.bird_rect = bird_rect
        
        self.x: int
        self.y: int
        
        self.top: int
        self.left: int
        self.bottom: int
        self.right: int
        
        self.topleft: tuple[int, int]
        self.topleft_x: int
        self.topleft_y: int
        
        self.bottomleft: tuple[int, int]
        self.bottomleft_x: int
        self.bottomleft_y: int
        
        self.topright: tuple[int, int]
        self.topright_x: int
        self.topright_y: int
        
        self.bottomright: tuple[int, int]
        self.bottomright_x: int
        self.bottomright_y: int
        
        self.midtop: tuple[int, int]
        self.midtop_x: int
        self.midtop_y: int
        
        self.midleft: tuple[int, int]
        self.midleft_x: int
        self.midleft_y: int
        
        self.midbottom: tuple[int, int]
        self.midbottom_x: int
        self.midbottom_y: int
        
        self.midright: tuple[int, int]
        self.midright_x: int
        self.midright_y: int
        
        self.center: tuple[int, int]
        self.centerx: int
        self.centery: int
        
        self.size: tuple[int, int]
        self.width: int
        self.height: int
        self.w: int
        self.h: int
        
        self.tuple_variables = ["topleft", "bottomleft", "topright", 
                                "bottomright", "midtop", "midleft", 
                                "midbottom", "midright"]
        
        
    def __getattr__(self, attr):
        """Retrieve the attribute dynamically from the underlying Rect object."""
        if hasattr(self.bird_rect, attr):
            return getattr(self.bird_rect, attr)
        
        for var in self.tuple_variables:
            if attr == f"{var}_x":
                return getattr(self.bird_rect, var)[0]
            elif attr == f"{var}_y":
                return getattr(self.bird_rect, var)[1]
            
        raise AttributeError(f"'BirdCoordinates' object has no attribute '{attr}'")
    
    def __setattr__(self, attr, value):
        """Set the attribute dynamically on the underlying Rect object."""
        if attr == 'bird_rect':
            return object.__setattr__(self, attr, value)
        elif hasattr(self.bird_rect, attr):
            return setattr(self.bird_rect, attr, value)
        
        for var in self.tuple_variables:
            if attr == f"{var}_x":
                return setattr(self.bird_rect, var, (value, self.__getattr__(f"{var}_y")))
            elif attr == f"{var}_y":
                return setattr(self.bird_rect, var, (self.__getattr__(f"{var}_x"), value))
            
        raise AttributeError(f"'BirdCoordinates' object has no attribute '{attr}'")
