<?php

// autoload_static.php @generated by Composer

namespace Composer\Autoload;

class ComposerStaticInit482a6b7ce19320f9c89846a83c6f0889
{
    public static $prefixLengthsPsr4 = array (
        'J' => 
        array (
            'Josantonius\\Session\\' => 20,
        ),
    );

    public static $prefixDirsPsr4 = array (
        'Josantonius\\Session\\' => 
        array (
            0 => __DIR__ . '/..' . '/josantonius/session/src',
        ),
    );

    public static $classMap = array (
        'Composer\\InstalledVersions' => __DIR__ . '/..' . '/composer/InstalledVersions.php',
    );

    public static function getInitializer(ClassLoader $loader)
    {
        return \Closure::bind(function () use ($loader) {
            $loader->prefixLengthsPsr4 = ComposerStaticInit482a6b7ce19320f9c89846a83c6f0889::$prefixLengthsPsr4;
            $loader->prefixDirsPsr4 = ComposerStaticInit482a6b7ce19320f9c89846a83c6f0889::$prefixDirsPsr4;
            $loader->classMap = ComposerStaticInit482a6b7ce19320f9c89846a83c6f0889::$classMap;

        }, null, ClassLoader::class);
    }
}
