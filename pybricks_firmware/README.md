# Pybricks firmware supporting UARTDevice

## EV3

The newest EV3 firmware already has `UARTDevice` enabled in the the latest firmware. 

## SPIKE Prime
This firmware was compiled with the option

`#define PYBRICKS_PY_IODEVICES_UART_DEVICE       (1)`

added to `mpconfigport.h`

Furthermore, the code has been changed to always enable power on pin 2 of the LPF2 port. This was done by adding the following code to `pybricks/iodevices/pb_type_uart_device.c`:


```
 // Get device, which inits UART port
    pb_type_uart_device_obj_t *self = mp_obj_malloc(pb_type_uart_device_obj_t, >

...


 // enable power on p2
    pbio_port_p1p2_set_power(self->port, PBIO_PORT_POWER_REQUIREMENTS_BATTERY_VOLTAGE_P2_POS);
 // line above was added	

    // Awaitables associated with reading and writing.
    self->write_iter = NULL;
    self->read_iter = NULL;
    self->wait_len = 0;

    return MP_OBJ_FROM_PTR(self);
}

```

## Technik hub

Recompiled the firmware with the option

`#define PYBRICKS_PY_IODEVICES_UART_DEVICE       (1)`

added to `mpconfigport.h`


