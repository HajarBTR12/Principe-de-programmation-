<?php
require_once __DIR__ . '/config/config.php';
require_once __DIR__ . '/services/StudentService.php';

$action = $_GET['action'] ?? 'list';

// Helper HTTP
function apiRequest(string $method, string $endpoint, array $data = []): ?array
{
    $url = API_BASE_URL . $endpoint;

    $context = stream_context_create([
        'http' => [
            'method'        => strtoupper($method),
            'header'        => "Content-Type: application/json\r\nAccept: application/json\r\n",
            'content'       => $data ? json_encode($data) : null,
            'ignore_errors' => true,
        ],
    ]);

    $response = @file_get_contents($url, false, $context);

    if ($response === false) {
        return null;
    }

    return json_decode($response, true);
}

// Routeur
switch ($action) {

    case 'list':
    default:
        $students = StudentService::getAllStudents() ?? [];
        require __DIR__ . '/views/students.php';
        break;

    case 'show':
        $id      = (int)($_GET['id'] ?? 0);
        $student = apiRequest('GET', '/students/' . $id);
        require __DIR__ . '/views/student_show.php';
        break;

    case 'search':
        $id      = (int)($_GET['id'] ?? 0);
        $student = apiRequest('GET', '/students/' . $id);
        require __DIR__ . '/views/student_show.php';
        break;

    case 'create':
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            $data = [
                'name' => trim($_POST['name'] ?? ''),
                'age'  => (int)($_POST['age'] ?? 0),
            ];
            apiRequest('POST', '/students', $data);
            header('Location: index.php?action=list');
            exit;
        }
        $mode    = 'create';
        $student = [];
        require __DIR__ . '/views/student_form.php';
        break;

    case 'edit':
        $id = (int)($_GET['id'] ?? 0);

        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            $data = [
                'name' => trim($_POST['name'] ?? ''),
                'age'  => (int)($_POST['age'] ?? 0),
            ];
            apiRequest('PUT', '/students/' . $id, $data);
            header('Location: index.php?action=list');
            exit;
        }

        $student = apiRequest('GET', '/students/' . $id) ?? [];
        $mode    = 'edit';
        require __DIR__ . '/views/student_form.php';
        break;

    case 'delete':
        $id = (int)($_GET['id'] ?? 0);
        apiRequest('DELETE', '/students/' . $id);
        header('Location: index.php?action=list');
        exit;
}
