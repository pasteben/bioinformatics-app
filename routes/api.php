<?php

use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Facades\Route;
use Illuminate\Validation\ValidationException;
use Symfony\Component\Process\Process;
use Symfony\Component\Process\Exception\ProcessFailedException;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    return $request->user();
});

Route::post('/count-nucleotides', function (Request $request) {
    $process = new Process(['python3', base_path().'/python-resources/CountNucleotides.py', $request->dna_string]);
    $process->run();

    // executes after the command finishes
    if (!$process->isSuccessful()) {
        throw new ProcessFailedException($process);
    }

    return json_decode($process->getOutput(), true);
});

Route::post('/reverse-complement', function (Request $request) {
    $process = new Process(['python3', base_path().'/python-resources/ReverseComplement.py', $request->dna_string]);
    $process->run();

    // executes after the command finishes
    if (!$process->isSuccessful()) {
        throw new ProcessFailedException($process);
    }

    return [
        'reverse_complement' => $process->getOutput()
    ];
});

Route::post('/transcribe', function (Request $request) {
    $process = new Process(['python3', base_path().'/python-resources/Transcribe.py', $request->dna_string]);
    $process->run();

    // executes after the command finishes
    if (!$process->isSuccessful()) {
        throw new ProcessFailedException($process);
    }

    return [
        'transcription' => $process->getOutput()
    ];
});

Route::post('/gc-content', function (Request $request) {
    $process = new Process(['python3', base_path().'/python-resources/GcContent.py', $request->dna_string]);
    $process->run();

    // executes after the command finishes
    if (!$process->isSuccessful()) {
        throw new ProcessFailedException($process);
    }

    return [
        'gc_content' => $process->getOutput()
    ];
});

Route::post('/gc-content-subsec', function (Request $request) {
    $process = new Process(['python3', base_path().'/python-resources/GcContentSubsec.py', $request->dna_string, $request->window]);
    $process->run();

    // executes after the command finishes
    if (!$process->isSuccessful()) {
        throw new ProcessFailedException($process);
    }

    return json_decode($process->getOutput(), true);
});

Route::post('/login', function (Request $request) {
    $request->validate([
        'email' => 'required|email',
        'password' => 'required',
        'device_name' => 'required',
    ]);

    $user = User::where('email', $request->email)->first();

    if (! $user || ! Hash::check($request->password, $user->password)) {
        throw ValidationException::withMessages([
            'email' => ['The provided credentials are incorrect.'],
        ]);
    }

    return $user->createToken($request->device_name)->plainTextToken;
});